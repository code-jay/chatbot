import { useEffect, useState } from "react";

function AdminDashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    loadStats();
  }, []);

  async function loadStats() {
    const token = localStorage.getItem("token");

    const res = await fetch(
      "http://127.0.0.1:8000/admin/stats",
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    const data = await res.json();
    setStats(data);
  }

  if (!stats) {
    return <div>Loading Dashboard...</div>;
  }

  return (
    <div className="admin-page">
      <h1>Admin Dashboard</h1>

      <div className="stats-grid">
        {Object.entries(stats).map(([key, value]) => (
          <div className="stat-card" key={key}>
            <h3>{key}</h3>
            <p>{value}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AdminDashboard;