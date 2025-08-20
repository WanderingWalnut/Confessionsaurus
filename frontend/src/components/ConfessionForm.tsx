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
        maxWidth: 520,
        mx: "auto",
        display: "flex",
        flexDirection: "column",
        gap: 4,
        mt: 2,
        backgroundColor: "rgba(255, 255, 255, 0.95)",
        backdropFilter: "blur(10px)",
        borderRadius: 4,
        padding: 5,
        boxShadow:
          "0 20px 60px rgba(220, 38, 38, 0.15), 0 8px 32px rgba(0, 0, 0, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.8)",
        border: "2px solid rgba(254, 202, 202, 0.6)",
        position: "relative",
        overflow: "hidden",
        "&::before": {
          content: '""',
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          height: "4px",
          background: "linear-gradient(90deg, #dc2626, #fca5a5, #dc2626)",
          borderRadius: "4px 4px 0 0",
        },
        transition: "all 0.3s ease-in-out",
        "&:hover": {
          transform: "translateY(-4px)",
          boxShadow:
            "0 25px 70px rgba(220, 38, 38, 0.2), 0 12px 40px rgba(0, 0, 0, 0.15)",
        },
      }}
    >
      <Typography
        variant="h5"
        align="center"
        fontWeight={700}
        mb={3}
        sx={{
          color: "#dc2626",
          fontFamily: "Comic Sans MS, cursive",
          textShadow: "2px 2px 4px rgba(220, 38, 38, 0.2)",
          fontSize: "1.75rem",
          letterSpacing: "0.5px",
          position: "relative",
          "&::after": {
            content: '""',
            position: "absolute",
            bottom: "-8px",
            left: "50%",
            transform: "translateX(-50%)",
            width: "60px",
            height: "3px",
            background: "linear-gradient(90deg, #dc2626, #fca5a5, #dc2626)",
            borderRadius: "2px",
          },
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
        minRows={8}
        variant="outlined"
        fullWidth
        InputProps={{
          sx: {
            backgroundColor: "rgba(254, 242, 242, 0.8)",
            color: "#991b1b",
            borderColor: "#fecaca",
            borderRadius: 3,
            fontSize: "16px",
            lineHeight: 1.6,
            "& fieldset": {
              borderColor: "#fecaca",
              borderWidth: 2,
              transition: "all 0.2s ease-in-out",
            },
            "&:hover fieldset": {
              borderColor: "#fca5a5",
              borderWidth: 2,
            },
            "&:hover": {
              backgroundColor: "rgba(254, 242, 242, 0.9)",
              transform: "translateY(-1px)",
              boxShadow: "0 4px 12px rgba(220, 38, 38, 0.1)",
            },
            "&.Mui-focused fieldset": {
              borderColor: "#dc2626",
              borderWidth: 3,
              boxShadow: "0 0 0 4px rgba(220, 38, 38, 0.1)",
            },
            "& .MuiInputBase-input": {
              fontFamily: "Comic Sans MS, cursive",
              fontSize: "16px",
              padding: "16px",
              "&::placeholder": {
                color: "#dc2626",
                opacity: 0.7,
              },
            },
          },
        }}
        InputLabelProps={{
          sx: {
            color: "#dc2626",
            fontFamily: "Comic Sans MS, cursive",
            fontWeight: 600,
            fontSize: "16px",
            "&.Mui-focused": {
              color: "#dc2626",
            },
          },
        }}
        FormHelperTextProps={{
          sx: {
            fontFamily: "Comic Sans MS, cursive",
            color: "#dc2626",
            opacity: 0.8,
            fontSize: "14px",
            marginLeft: 0,
          },
        }}
        helperText="Your confession will be posted anonymously on Instagram"
      />

      {error && (
        <Box
          sx={{
            backgroundColor: "rgba(254, 226, 226, 0.8)",
            border: "2px solid #fca5a5",
            borderRadius: 3,
            padding: 2,
            textAlign: "center",
          }}
        >
          <Typography
            color="error"
            sx={{
              fontFamily: "Comic Sans MS, cursive",
              fontWeight: 600,
              fontSize: "16px",
            }}
          >
            🦕 Oops! {error} 🦖
          </Typography>
        </Box>
      )}

      <Button
        type="submit"
        variant="contained"
        size="large"
        disabled={isSubmitting}
        sx={{
          fontWeight: 700,
          backgroundColor: "linear-gradient(135deg, #dc2626 0%, #b91c1c 100%)",
          background: "linear-gradient(135deg, #dc2626 0%, #b91c1c 100%)",
          color: "#fff",
          fontFamily: "Comic Sans MS, cursive",
          fontSize: "18px",
          borderRadius: 3,
          padding: "16px 32px",
          boxShadow:
            "0 8px 24px rgba(220, 38, 38, 0.3), 0 4px 12px rgba(0, 0, 0, 0.1)",
          border: "2px solid rgba(254, 202, 202, 0.6)",
          position: "relative",
          overflow: "hidden",
          transition: "all 0.3s ease-in-out",
          "&::before": {
            content: '""',
            position: "absolute",
            top: 0,
            left: "-100%",
            width: "100%",
            height: "100%",
            background:
              "linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent)",
            transition: "left 0.5s ease-in-out",
          },
          "&:hover": {
            background: "linear-gradient(135deg, #b91c1c 0%, #991b1b 100%)",
            boxShadow:
              "0 12px 32px rgba(220, 38, 38, 0.4), 0 6px 16px rgba(0, 0, 0, 0.15)",
            transform: "translateY(-2px)",
            "&::before": {
              left: "100%",
            },
          },
          "&:active": {
            transform: "translateY(0px)",
            boxShadow: "0 4px 16px rgba(220, 38, 38, 0.3)",
          },
          "&:disabled": {
            background: "linear-gradient(135deg, #fca5a5 0%, #f87171 100%)",
            color: "#991b1b",
            transform: "none",
            boxShadow: "0 4px 16px rgba(220, 38, 38, 0.2)",
          },
        }}
      >
        {isSubmitting ? "🦕 Submitting..." : "🦖 Submit Confession!"}
      </Button>
    </Box>
  );
};

export default ConfessionForm;
