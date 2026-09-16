import os
import time
import random
import logging

logger = logging.getLogger("db_monitor")

class DBMonitor:
    def __init__(self):
        self.pg_url = os.getenv("POSTGRES_URL") or os.getenv("DATABASE_URL")
        self.active_scenario = "LOCK_CONTENTION"  # Default scenario for demo
        self.last_poll_time = time.time()
        
    def set_scenario(self, scenario_name):
        valid = ["LOCK_CONTENTION", "POOL_EXHAUSTION", "RUNAWAY_QUERY", "HEALTHY"]
        if scenario_name in valid:
            self.active_scenario = scenario_name
            logger.info(f"DB Monitor scenario changed to: {scenario_name}")
            return True
        return False

    def poll_metrics(self):
        self.last_poll_time = time.time()
        
        # Try real PostgreSQL if configured
        if self.pg_url:
            try:
                import psycopg2
                conn = psycopg2.connect(self.pg_url, connect_timeout=3)
                cursor = conn.cursor()
                
                # Query active & blocked sessions
                cursor.execute("""
                    SELECT 
                        count(*) as total_active,
                        count(*) FILTER (WHERE waiting OR state = 'active' AND wait_event IS NOT NULL) as blocked
                    FROM pg_stat_activity 
                    WHERE state = 'active';
                """)
                active, blocked = cursor.fetchone()
                
                # Query cache hit ratio
                cursor.execute("""
                    SELECT 
                        sum(heap_blks_hit) / nullif(sum(heap_blks_hit) + sum(heap_blks_read),0) * 100 as cache_hit_ratio
                    FROM pg_stat_database;
                """)
                cache_hit = cursor.fetchone()[0] or 99.4
                
                cursor.close()
                conn.close()
                
                return {
                    "PNCPRD01": {
                        "active_sessions": active,
                        "blocked_sessions": blocked,
                        "cache_hit_ratio": round(float(cache_hit), 1),
                        "avg_query_time_ms": 120 if blocked == 0 else 840
                    }
                }
            except Exception as e:
                logger.warning(f"Real Postgres connect failed ({e}), using synthetic engine")
        
        # Synthetic simulation engine fallback
        return self._get_synthetic_metrics()

    def _get_synthetic_metrics(self):
        if self.active_scenario == "LOCK_CONTENTION":
            return {
                "PNCPRD01": {
                    "status": "AT_RISK",
                    "risk_score": 88,
                    "status_desc": "Primary cluster · Lock contention detected",
                    "active_sessions": 42 + random.randint(-2, 2),
                    "blocked_sessions": 4,
                    "cache_hit_ratio": 99.4,
                    "avg_query_time_ms": 840 + random.randint(-30, 30),
                    "anomaly": {
                        "type": "LOCK_CONTENTION",
                        "database": "PNCPRD01",
                        "title": "Lock contention on public.orders (PID 48219 holding exclusive tuple lock)",
                        "target_table": "public.orders",
                        "blocking_pid": 48219,
                        "wait_event": "Lock:tuple",
                        "waiting_count": 4,
                        "duration_sec": 184
                    }
                },
                "RECON_DB": {
                    "status": "HEALTHY",
                    "risk_score": 12,
                    "status_desc": "Reconciliation service · Healthy",
                    "active_sessions": 14,
                    "blocked_sessions": 0,
                    "cache_hit_ratio": 99.8,
                    "avg_query_time_ms": 18,
                    "anomaly": None
                },
                "MBL_STG": {
                    "status": "HEALTHY",
                    "risk_score": 8,
                    "status_desc": "Mobile staging · Healthy",
                    "active_sessions": 6,
                    "blocked_sessions": 0,
                    "cache_hit_ratio": 99.9,
                    "avg_query_time_ms": 12,
                    "anomaly": None
                }
            }
        elif self.active_scenario == "POOL_EXHAUSTION":
            return {
                "PNCPRD01": {
                    "status": "AT_RISK",
                    "risk_score": 92,
                    "status_desc": "Primary cluster · Connection pool exhaustion",
                    "active_sessions": 98,
                    "blocked_sessions": 24,
                    "cache_hit_ratio": 96.2,
                    "avg_query_time_ms": 1420,
                    "anomaly": {
                        "type": "POOL_EXHAUSTION",
                        "database": "PNCPRD01",
                        "title": "Max connections reached (98/100 active connections in ClientRead wait)",
                        "target_table": "global_pool",
                        "blocking_pid": None,
                        "wait_event": "ClientRead",
                        "waiting_count": 24,
                        "duration_sec": 95
                    }
                },
                "RECON_DB": {
                    "status": "HEALTHY",
                    "risk_score": 14,
                    "status_desc": "Reconciliation service · Healthy",
                    "active_sessions": 16,
                    "blocked_sessions": 0,
                    "cache_hit_ratio": 99.7,
                    "avg_query_time_ms": 22,
                    "anomaly": None
                },
                "MBL_STG": {
                    "status": "HEALTHY",
                    "risk_score": 5,
                    "status_desc": "Mobile staging · Healthy",
                    "active_sessions": 8,
                    "blocked_sessions": 0,
                    "cache_hit_ratio": 99.9,
                    "avg_query_time_ms": 14,
                    "anomaly": None
                }
            }
        elif self.active_scenario == "RUNAWAY_QUERY":
            return {
                "PNCPRD01": {
                    "status": "AT_RISK",
                    "risk_score": 78,
                    "status_desc": "Primary cluster · Runaway unindexed sequential scan",
                    "active_sessions": 31,
                    "blocked_sessions": 0,
                    "cache_hit_ratio": 84.1,
                    "avg_query_time_ms": 2100,
                    "anomaly": {
                        "type": "RUNAWAY_QUERY",
                        "database": "PNCPRD01",
                        "title": "Runaway query PID 31092 scanning 42M rows without index on audit_logs",
                        "target_table": "public.audit_logs",
                        "blocking_pid": 31092,
                        "wait_event": "DataFileRead",
                        "waiting_count": 0,
                        "duration_sec": 412
                    }
                },
                "RECON_DB": {
                    "status": "HEALTHY",
                    "risk_score": 10,
                    "status_desc": "Reconciliation service · Healthy",
                    "active_sessions": 12,
                    "blocked_sessions": 0,
                    "cache_hit_ratio": 99.8,
                    "avg_query_time_ms": 16,
                    "anomaly": None
                },
                "MBL_STG": {
                    "status": "HEALTHY",
                    "risk_score": 6,
                    "status_desc": "Mobile staging · Healthy",
                    "active_sessions": 5,
                    "blocked_sessions": 0,
                    "cache_hit_ratio": 99.9,
                    "avg_query_time_ms": 11,
                    "anomaly": None
                }
            }
        else: # HEALTHY
            return {
                "PNCPRD01": {
                    "status": "HEALTHY",
                    "risk_score": 10,
                    "status_desc": "Primary cluster · Healthy",
                    "active_sessions": 12,
                    "blocked_sessions": 0,
                    "cache_hit_ratio": 99.8,
                    "avg_query_time_ms": 14,
                    "anomaly": None
                },
                "RECON_DB": {
                    "status": "HEALTHY",
                    "risk_score": 12,
                    "status_desc": "Reconciliation service · Healthy",
                    "active_sessions": 14,
                    "blocked_sessions": 0,
                    "cache_hit_ratio": 99.8,
                    "avg_query_time_ms": 18,
                    "anomaly": None
                },
                "MBL_STG": {
                    "status": "HEALTHY",
                    "risk_score": 8,
                    "status_desc": "Mobile staging · Healthy",
                    "active_sessions": 6,
                    "blocked_sessions": 0,
                    "cache_hit_ratio": 99.9,
                    "avg_query_time_ms": 12,
                    "anomaly": None
                }
            }

    def get_fleet_summary(self):
        metrics = self.poll_metrics()
        fleet = []
        for db_name, data in metrics.items():
            fleet.append({
                "name": db_name,
                "status": data["status"],
                "risk_score": data["risk_score"],
                "status_desc": data["status_desc"]
            })
        return fleet

    def get_active_anomaly(self):
        metrics = self.poll_metrics()
        for db_name, data in metrics.items():
            if data.get("anomaly"):
                return data["anomaly"]
        return None
