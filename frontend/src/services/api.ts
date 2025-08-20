const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://5dpcxowms8.execute-api.us-east-2.amazonaws.com/Prod';

export const submitConfession = async (content: string) => {
  const response = await fetch(`${API_BASE_URL}/api/confess/submit`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ content }),
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  return response.json();
};
