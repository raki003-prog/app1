import { useState } from "react";

function App() {
  const [customerId, setCustomerId] = useState("");
  const [customerData, setCustomerData] = useState(null);
  const [error, setError] = useState(false);

  const getCustomer = async () => {
    setError(false);
    setCustomerData(null);
    try {
      const res = await fetch(`http://localhost:8000/customers/${customerId}`);
      if (!res.ok) throw new Error("Fetch failed");
      const data = await res.json();
      setCustomerData(data);
    } catch (err) {
      setError(true);
    }
  };

  return (
    <div style={{ padding: "2rem", color: "#fff", backgroundColor: "#222" }}>
      <h1>Customer Info</h1>
      <input
        type="text"
        value={customerId}
        onChange={(e) => setCustomerId(e.target.value)}
        placeholder="Enter customer ID"
      />
      <button onClick={getCustomer}>Get Customer</button>

      {error && <p style={{ color: "red" }}>Error fetching customer</p>}

      {customerData && (
        <pre style={{ color: "#0f0" }}>{JSON.stringify(customerData, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;
