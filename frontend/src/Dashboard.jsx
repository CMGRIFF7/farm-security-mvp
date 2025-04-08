// src/Dashboard.jsx — Save as frontend/src/Dashboard.jsx
// ----------------------------
import React, { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

const socket = io(import.meta.env.VITE_SOCKET_URL);

export default function Dashboard() {
  const [alerts, setAlerts] = useState([]);
  const [assets, setAssets] = useState([]);
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    socket.on('connect', () => {
      console.log('✅ Socket connected to backend');
    });
    socket.on('alert', (data) => {
      setAlerts((prev) => [data, ...prev.slice(0, 4)]);
    });

    socket.on('asset_update', (data) => {
      setAssets((prev) => [data, ...prev.slice(0, 9)]);
    });

    socket.on('log', (data) => {
      setLogs((prev) => [data, ...prev.slice(0, 19)]);
    });

    return () => {
      socket.off('alert');
      socket.off('asset_update');
      socket.off('log');
    };
  }, []);

  const simulateEvent = async () => {
    try {
      const res = await fetch('https://farm-security-backend.onrender.com/api/simulate');
      if (!res.ok) throw new Error('Simulation failed');
      console.log('Simulation triggered');
    } catch (err) {
      console.error('Error triggering simulation:', err);
    }
  };

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">Farm Security Dashboard</h1>

      <button
        onClick={simulateEvent}
        className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Trigger Simulation
      </button>

      <section>
        <h2 className="text-xl font-semibold">Recent Alerts</h2>
        <ul className="list-disc list-inside">
          {alerts.map((alert, index) => (
            <li key={index}>{alert}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2 className="text-xl font-semibold">Latest Asset Movements</h2>
        <ul className="list-disc list-inside">
          {assets.map((asset, index) => (
            <li key={index}>{JSON.stringify(asset)}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2 className="text-xl font-semibold">System Logs</h2>
        <ul className="text-sm font-mono bg-gray-100 p-2 rounded">
          {logs.map((log, index) => (
            <li key={index}>{log}</li>
          ))}
        </ul>
      </section>
    </div>
  );
}
