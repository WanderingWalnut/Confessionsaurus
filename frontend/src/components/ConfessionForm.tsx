import React, { useState } from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import { submitConfession } from "../services/api";

const ConfessionForm: React.FC = () => {
  const [content, setContent] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError(null);

    try {
      const data = await submitConfession(content);
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
        backgroundColor: "#fff",
        borderRadius: 3,
        padding: 4,
        boxShadow: "0 8px 32px rgba(220, 38, 38, 0.1)",
        border: "3px solid #fecaca",
      }}
    >
      <Typography
        variant="h5"
        align="center"
        fontWeight={700}
        mb={2}
        sx={{
          color: "#dc2626",
          fontFamily: "Comic Sans MS, cursive",
          textShadow: "2px 2px 4px rgba(220, 38, 38, 0.2)",
        }}
      >
        🦕 Share Your Prehistoric Secret! 🦖
      </Typography>
      <TextField
        id="content"
        name="content"
        label="What's on your mind, dinosaur friend?"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        required
        multiline
        minRows={6}
        variant="outlined"
        fullWidth
        InputProps={{
          sx: {
            backgroundColor: "#fef2f2",
            color: "#991b1b",
            borderColor: "#fecaca",
            borderRadius: 2,
            "& fieldset": {
              borderColor: "#fecaca",
              borderWidth: 2,
            },
            "&:hover fieldset": {
              borderColor: "#fca5a5",
            },
            "&.Mui-focused fieldset": {
              borderColor: "#dc2626",
              borderWidth: 3,
            },
            "& .MuiInputBase-input": {
              fontFamily: "Comic Sans MS, cursive",
              fontSize: "16px",
            },
          },
        }}
        InputLabelProps={{
          sx: {
            color: "#dc2626",
            fontFamily: "Comic Sans MS, cursive",
            fontWeight: 600,
          },
        }}
      />
      {error && (
        <Typography
          color="error"
          mb={1}
          sx={{
            fontFamily: "Comic Sans MS, cursive",
            fontWeight: 600,
          }}
        >
          🦕 Oops! {error} 🦖
        </Typography>
      )}
      <Button
        type="submit"
        variant="contained"
        size="large"
        disabled={isSubmitting}
        sx={{
          fontWeight: 700,
          backgroundColor: "#dc2626",
          color: "#fff",
          fontFamily: "Comic Sans MS, cursive",
          fontSize: "18px",
          borderRadius: 3,
          padding: "12px 24px",
          boxShadow: "0 4px 16px rgba(220, 38, 38, 0.3)",
          "&:hover": {
            backgroundColor: "#b91c1c",
            boxShadow: "0 6px 20px rgba(220, 38, 38, 0.4)",
            transform: "translateY(-2px)",
          },
          "&:disabled": {
            backgroundColor: "#fca5a5",
            color: "#991b1b",
          },
          border: "3px solid #fecaca",
        }}
      >
        {isSubmitting ? "🦕 Submitting..." : "🦖 Submit Confession!"}
      </Button>
    </Box>
  );
};

export default ConfessionForm;
