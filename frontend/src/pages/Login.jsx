import { useState } from "react";
import { loginUser } from "../services/api";
import { useNavigate, Link } from "react-router-dom";

function Login() {
    const [form, setForm] = useState({
        email: "",
        password: ""
    });

    const navigate = useNavigate();

    const handleChange = (e) => {
        setForm({...form, [e.target.name]: e.target.value});
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await loginUser(form);
            localStorage.setItem("token", res.data.access_token);
            alert("Login successful");
            navigate("/dashboard");
        } catch (error) {
            alert("Invalid credentials");
        }
    };

    return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
        <form onSubmit={handleSubmit} className="bg-white p-8 rounded-xl shadow-md w-80">
        <h2 className="text-2xl font-bold mb-6 text-center">IncomeGuard Login</h2>

        <input
            className="w-full p-2 mb-3 border rounded"
            name="email"
            placeholder="Email"
            onChange={handleChange}
        />

        <input
            className="w-full p-2 mb-4 border rounded"
            name="password"
            type="password"
            placeholder="Password"
            onChange={handleChange}
        />

        <button className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700">
            Login
        </button>

        <p className="mt-4 text-sm text-center">
            Not registered?{" "}
            <Link className="text-blue-600" to="/register">
            Register here
            </Link>
        </p>
        </form>
    </div>
    );
}

export default Login;