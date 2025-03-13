// Dashboard.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [prediction, setPrediction] = useState(null);
  const [anomaly, setAnomaly] = useState(null);
  const transactionId = "tx12345"; // Example transaction id

  useEffect(() => {
    const fetchPrediction = async () => {
      try {
        const res = await axios.get(`/predict-payment-delay?transaction_id=${transactionId}`);
        setPrediction(res.data.predicted_delay_days);
      } catch (error) {
        console.error("Error fetching payment prediction", error);
      }
    };

    const fetchAnomaly = async () => {
      try {
        const res = await axios.get(`/detect-anomaly?transaction_id=${transactionId}`);
        setAnomaly(res.data.anomaly_detected);
      } catch (error) {
        console.error("Error fetching anomaly detection", error);
      }
    };

    fetchPrediction();
    fetchAnomaly();
  }, [transactionId]);

  return (
    <div>
      <h1>Payment Dashboard</h1>
      <div>
        <h2>Payment Delay Prediction</h2>
        {prediction !== null ? (
          <p>Predicted Delay: {prediction} days</p>
        ) : (
          <p>Loading...</p>
        )}
      </div>
      <div>
        <h2>Anomaly Detection</h2>
        {anomaly !== null ? (
          <p>Anomaly Detected: {anomaly ? "Yes" : "No"}</p>
        ) : (
          <p>Loading...</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
