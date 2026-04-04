import { useState } from "react";
import { createPolicy } from "../services/api";

function BuyPolicy() {
    const [form, setForm] = useState({
        user_id: "",
        week_start_date: "",
        week_end_date: "",
        location: "",
        planned_work_hours: ""
    });

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await createPolicy(form);
            alert("Policy created. Premium: " + res.data.premium);
        } catch (error) {
            alert("Error creating policy");
        }
    };

    return (
        <div>
            <h2>Buy Weekly Policy</h2>
            <form onSubmit={handleSubmit}>
                <input name="user_id" placeholder="User ID" onChange={handleChange} />
                <input name="week_start_date" type="date" onChange={handleChange} />
                <input name="week_end_date" type="date" onChange={handleChange} />
                <input name="location" placeholder="Location" onChange={handleChange} />
                <input name="planned_work_hours" placeholder="Work Hours" onChange={handleChange} />
                <button type="submit">Create Policy</button>
            </form>
        </div>
    );
}

export default BuyPolicy;