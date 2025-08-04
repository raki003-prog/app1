import React from 'react';

const CustomerCard = ({ customer }) => {
  return (
    <div className="col-md-4 mb-4">
      <div className="card h-100 shadow-sm">
        <div className="card-body">
          <h5 className="card-title">{customer.name || "Unknown"}</h5>
          <p className="card-text">
            <strong>Email:</strong> {customer.email || "N/A"}<br />
            <strong>Orders:</strong> {customer.order_count}
          </p>
        </div>
      </div>
    </div>
  );
};

export default CustomerCard;
