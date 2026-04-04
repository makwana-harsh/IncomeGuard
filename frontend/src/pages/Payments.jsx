import { useState } from "react";
import { getPayments } from "../services/api";

function Payments() {
    const [userId, setUserId] = useState("");
    const [payments, setPayments] = useState([]);

    const fetchPayments = async () => {
        const res = await getPayments(userId);
        setPayments(res.data);
    };

    return (
        <div>
            <h2>Payments</h2>
            <input
                placeholder="Enter User ID"
                onChange={(e) => setUserId(e.target.value)}
            />
            <button onClick={fetchPayments}>Get Payments</button>

            <table>
                <thead>
                    <tr>
                        <th>Amount</th>
                        <th>Status</th>
                        <th>Method</th>
                        <th>Transaction ID</th>
                    </tr>
                </thead>
                <tbody>
                    {payments.map((p) => (
                        <tr key={p.payment_id}>
                            <td>{p.amount}</td>
                            <td>{p.payment_status}</td>
                            <td>{p.payment_method}</td>
                            <td>{p.transaction_id}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Payments;