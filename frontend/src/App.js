import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import BuyPolicy from "./pages/BuyPolicy";
import Schedule from "./pages/Schedule";
import Claims from "./pages/Claims";
import Payments from "./pages/Payments";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/buy-policy" element={<BuyPolicy />} />
                <Route path="/schedule" element={<Schedule />} />
                <Route path="/claims" element={<Claims />} />
                <Route path="/payments" element={<Payments />} />
            </Routes>
        </Router>
    );
}

export default App;