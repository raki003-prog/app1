import React, { useEffect, useState } from 'react';
import CustomerCard from './CustomerCard';
import './App.css';

function App() {
  const [customers, setCustomers] = useState([]);
  const [query, setQuery] = useState('');

  useEffect(() => {
    fetch('http://127.0.0.1:8000/customers')
      .then(res => res.json())
      .then(async data => {
        const detailed = await Promise.all(
          data.customers.map(c =>
            fetch(`http://127.0.0.1:8000/customers/${c.user_id}`).then(res => res.json())
          )
        );
        setCustomers(detailed);
      });
  }, []);

  const filtered = customers.filter(c =>
    c.name?.toLowerCase().includes(query.toLowerCase()) ||
    c.email?.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div className="container">
      <h1 className="my-4">Customer List</h1>
      <input
        type="text"
        className="form-control mb-3"
        placeholder="Search by name or email..."
        value={query}
        onChange={e => setQuery(e.target.value)}
      />
      <div className="row">
        {filtered.map((c, i) => (
          <CustomerCard key={i} customer={c} />
        ))}
      </div>
    </div>
  );
}
export default App;
