import { useState } from "react";
import Login from "./Login";
import Upload from "./Upload";
import "./index.css";

function App() {
  const [token, setToken] = useState(null);

  return (
    <div className="container">
      <h1>VoiceGuardAI</h1>

      {!token ? (
        <Login onLogin={setToken} />
      ) : (
        <Upload token={token} />
      )}

      <div className="footer">
        AI-powered deepfake detection
      </div>
    </div>
  );
}

export default App;

