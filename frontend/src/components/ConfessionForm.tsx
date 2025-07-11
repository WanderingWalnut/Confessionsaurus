import React, { useState } from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";

const ConfessionForm: React.FC = () => {
  const [content, setContent] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/api/confess/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          content: content,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Response: ", data);

      // Only reset form on success
      setContent("");
    } catch (error) {
      console.error("An error occurred: ", error);
      setError("Failed to submit confession. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Box
      component="form"
      onSubmit={handleSubmit}
      sx={{
        maxWidth: 480,
        mx: "auto",
        display: "flex",
        flexDirection: "column",
        gap: 3,
        mt: 2,
      }}
    >
      <Typography variant="h6" align="center" fontWeight={600} mb={1}>
        Your Confession
      </Typography>
      <TextField
        id="content"
        name="content"
        label="Share your thoughts..."
        value={content}
        onChange={(e) => setContent(e.target.value)}
        //     ↑        ↑                    ↑
        //   "Watch"  "When"              "Get the text"
        //   for      user types           from the box
        //   changes  in the box           and save it
        required
        multiline
        minRows={6}
        variant="outlined"
        fullWidth
        InputProps={{
          sx: {
            backgroundColor: "#222",
            color: "#fff",
            borderColor: "#444",
            "& fieldset": {
              borderColor: "#444",
            },
            "&:hover fieldset": {
              borderColor: "#666",
            },
            "&.Mui-focused fieldset": {
              borderColor: "#fff",
            },
          },
        }}
        InputLabelProps={{
          sx: { color: "#aaa" },
        }}
      />
      {error && (
        <Typography color="error" mb={1}>
          {error}
        </Typography>
      )}
      <Button
        type="submit"
        variant="contained"
        size="large"
        disabled={isSubmitting}
        sx={{
          fontWeight: 600,
          backgroundColor: "#222",
          color: "#fff",
          "&:hover": {
            backgroundColor: "#111",
          },
          border: "1px solid #444",
        }}
      >
        {isSubmitting ? "Submitting..." : "Submit Confession"}
      </Button>
    </Box>
  );
};

export default ConfessionForm;
