import { useState } from "react";
import { addSchedule } from "../services/api";

function Schedule() {
    const [form, setForm] = useState({
        user_id: "",
        date: "",
        start_time: "",
        end_time: "",
        location: ""
    });

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await addSchedule(form);
            alert("Schedule added");
        } catch (error) {
            alert("Error adding schedule");
        }
    };

    return (
        <div>
            <h2>Add Work Schedule</h2>
            <form onSubmit={handleSubmit}>
                <input name="user_id" placeholder="User ID" onChange={handleChange} />
                <input name="date" type="date" onChange={handleChange} />
                <input name="start_time" type="time" onChange={handleChange} />
                <input name="end_time" type="time" onChange={handleChange} />
                <input name="location" placeholder="Location" onChange={handleChange} />
                <button type="submit">Add Schedule</button>
            </form>
        </div>
    );
}

export default Schedule;