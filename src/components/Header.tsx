import React from 'react';

interface HeaderProps {
  lastPolledSecAgo: number;
}

export const Header: React.FC<HeaderProps> = ({ lastPolledSecAgo }) => {
  return (
    <header className="header-container">
      <div className="brand-group">
        <span className="brand-title">dbpulse</span>
        <span className="brand-subtitle">Postgres reliability agent</span>
      </div>
      <div className="status-badge">
        <span className="pulse-dot"></span>
        <span>last polled {lastPolledSecAgo}s ago</span>
      </div>
    </header>
  );
};
