import { useState } from "react";
import { detectMedia } from "./api";

export default function Upload({ token }) {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await detectMedia(formData, token);
    setResult(res.data);
  };

  return (
    <>
      <h2>Upload Media</h2>

      <div className="upload-box">
        <input type="file" onChange={e => setFile(e.target.files[0])} />
      </div>

      <button onClick={handleUpload}>Detect Deepfake</button>

      {result && (
        <div className={`result ${result.prediction.toLowerCase()}`}>
          <p><b>Prediction:</b> {result.prediction}</p>
          <p className="confidence">
            Confidence: {Math.round(result.confidence * 100)}%
          </p>
        </div>
      )}
    </>
  );
}
