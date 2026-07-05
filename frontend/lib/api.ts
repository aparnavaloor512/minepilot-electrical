// Shape of the response we expect from the backend /health route
export type HealthResponse = {
  status: string;
};

// Calls the FastAPI backend and returns its health status
export async function getBackendHealth(): Promise<HealthResponse> {
  const response = await fetch("http://localhost:8000/health");

  if (!response.ok) {
    throw new Error("Failed to connect to backend");
  }

  return response.json();
}