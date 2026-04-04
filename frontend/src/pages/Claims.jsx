import { useState } from "react";
import { getClaims } from "../services/api";

function Claims() {
    const [userId, setUserId] = useState("");
    const [claims, setClaims] = useState([]);

    const fetchClaims = async () => {
        const res = await getClaims(userId);
        setClaims(res.data);
    };

    return (
        <div>
            <h2>Claims</h2>
            <input
                placeholder="Enter User ID"
                onChange={(e) => setUserId(e.target.value)}
            />
            <button onClick={fetchClaims}>Get Claims</button>

            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Disruption</th>
                        <th>Payout</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {claims.map((c) => (
                        <tr key={c.claim_id}>
                            <td>{c.date}</td>
                            <td>{c.disruption_type}</td>
                            <td>{c.payout_amount}</td>
                            <td>{c.claim_status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Claims;