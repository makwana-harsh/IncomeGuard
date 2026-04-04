import { useState } from "react";
import { registerUser } from "../services/api";
import { useNavigate, Link } from "react-router-dom";

function Register() {
    const [form, setForm] = useState({
        name: "",
        phone: "",
        email: "",
        password: "",
        vehicle_type: "",
        platform: ""
    });

    const navigate = useNavigate();

    const handleChange = (e) => {
        setForm({...form, [e.target.name]: e.target.value});
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await registerUser(form);
            alert("Registered successfully");
            navigate("/login");
        } catch (error) {
            alert("Error registering");
        }
    };

    return (
        <div>
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <input required name="name" placeholder="Name" onChange={handleChange} />
                <input required name="phone" placeholder="Phone" onChange={handleChange} />
                <input required name="email" placeholder="Email" onChange={handleChange} />
                <input required name="password" type="password" placeholder="Password" onChange={handleChange} />
                <input required name="vehicle_type" placeholder="Vehicle Type" onChange={handleChange} />
                <input required name="platform" placeholder="Platform (Uber/Ola/etc)" onChange={handleChange} />
                <button type="submit">Register</button>
            </form>

            <p>
                Already registered? <Link to="/login">Login here</Link>
            </p>
        </div>
    );
}

export default Register;