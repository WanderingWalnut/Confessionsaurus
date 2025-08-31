import React, { useState, useRef, useEffect } from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import { submitConfession } from "../services/api";

const ConfessionForm: React.FC = () => {
  const [content, setContent] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const titleContainerRef = useRef<HTMLDivElement | null>(null);
  const titleRef = useRef<HTMLDivElement | null>(null);
  const [titleScale, setTitleScale] = useState(1);

  useEffect(() => {
    const updateScale = () => {
      const containerWidth = titleContainerRef.current?.clientWidth ?? 0;
      const titleWidth = titleRef.current?.scrollWidth ?? 0;
      if (containerWidth > 0 && titleWidth > 0) {
        const scale = Math.min(1, (containerWidth - 8) / titleWidth);
        setTitleScale(scale);
      } else {
        setTitleScale(1);
      }
    };

    let ro: ResizeObserver | null = null;
    if (typeof ResizeObserver !== "undefined") {
      ro = new ResizeObserver(updateScale);
      if (titleContainerRef.current) ro.observe(titleContainerRef.current);
      if (titleRef.current) ro.observe(titleRef.current);
    }
    window.addEventListener("resize", updateScale);
    updateScale();

    return () => {
      ro?.disconnect();
      window.removeEventListener("resize", updateScale);
    };
  }, []);

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
        width: { xs: "82%", sm: "100%" },
        maxWidth: { xs: "82%", sm: 480, md: 520 },
        mx: "auto",
        alignSelf: "center",
        boxSizing: "border-box",
        display: "flex",
        flexDirection: "column",
        gap: { xs: 3, sm: 4 },
        mt: { xs: 1, sm: 2 },
        backgroundColor: "rgba(255, 255, 255, 0.95)",
        backdropFilter: "blur(10px)",
        borderRadius: { xs: 2, sm: 3, md: 4 },
        padding: { xs: 2.5, sm: 4, md: 5 },
        boxShadow: {
          xs: "0 10px 24px rgba(220, 38, 38, 0.15), 0 4px 16px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.8)",
          sm: "0 20px 60px rgba(220, 38, 38, 0.15), 0 8px 32px rgba(0, 0, 0, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.8)",
        },
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
          transform: { xs: "none", sm: "translateY(-4px)" },
          boxShadow:
            "0 25px 70px rgba(220, 38, 38, 0.2), 0 12px 40px rgba(0, 0, 0, 0.15)",
        },
      }}
    >
      <Box
        ref={titleContainerRef}
        sx={{
          width: "100%",
          display: "flex",
          justifyContent: "center",
          overflow: "hidden",
        }}
      >
        <Typography
          ref={titleRef}
          variant="h5"
          align="center"
          fontWeight={700}
          mb={{ xs: 2, sm: 3 }}
          sx={{
            color: "#dc2626",
            fontFamily: "'Comic Neue', 'Comic Sans MS', cursive",
            textShadow: "2px 2px 4px rgba(220, 38, 38, 0.2)",
            fontSize: { xs: "1.1rem", sm: "1.25rem", md: "1.75rem" },
            letterSpacing: "0.5px",
            position: "relative",
            lineHeight: 1.2,
            whiteSpace: "nowrap",
            display: "inline-block",
            transform: `scale(${titleScale})`,
            transformOrigin: "center",
            "&::after": {
              content: '""',
              position: "absolute",
              bottom: "-8px",
              left: "50%",
              transform: "translateX(-50%)",
              width: { xs: "28px", sm: "40px", md: "60px" },
              height: "3px",
              background: "linear-gradient(90deg, #dc2626, #fca5a5, #dc2626)",
              borderRadius: "2px",
            },
          }}
        >
          🦕 Share Your Prehistoric Secret! 🦖
        </Typography>
      </Box>

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
            backgroundColor: "rgba(254, 242, 242, 0.8)",
            color: "#991b1b",
            borderColor: "#fecaca",
            borderRadius: { xs: 2, sm: 3 },
            fontSize: { xs: "14px", sm: "15px", md: "16px" },
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
              transform: { xs: "none", sm: "translateY(-1px)" },
              boxShadow: "0 4px 12px rgba(220, 38, 38, 0.1)",
            },
            "&.Mui-focused fieldset": {
              borderColor: "#dc2626",
              borderWidth: 3,
              boxShadow: "0 0 0 4px rgba(220, 38, 38, 0.1)",
            },
            "& .MuiInputBase-input": {
              fontFamily: "'Comic Neue', 'Comic Sans MS', cursive",
              fontSize: { xs: "14px", sm: "15px", md: "16px" },
              padding: { xs: "12px", sm: "14px", md: "16px" },
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
            fontFamily: "'Comic Neue', 'Comic Sans MS', cursive",
            fontWeight: 600,
            fontSize: { xs: "14px", sm: "15px", md: "16px" },
            "&.Mui-focused": {
              color: "#dc2626",
            },
          },
        }}
        FormHelperTextProps={{
          sx: {
            fontFamily: "'Comic Neue', 'Comic Sans MS', cursive",
            color: "#dc2626",
            opacity: 0.8,
            fontSize: { xs: "12px", sm: "13px", md: "14px" },
            marginLeft: 0,
            textAlign: { xs: "center", sm: "left" },
          },
        }}
        helperText="Your confession will be posted anonymously on Instagram"
      />

      {error && (
        <Box
          sx={{
            backgroundColor: "rgba(254, 226, 226, 0.8)",
            border: "2px solid #fca5a5",
            borderRadius: { xs: 2, sm: 3 },
            padding: { xs: 1.5, sm: 2 },
            textAlign: "center",
          }}
        >
          <Typography
            color="error"
            sx={{
              fontFamily: "'Comic Neue', 'Comic Sans MS', cursive",
              fontWeight: 600,
              fontSize: { xs: "14px", sm: "15px", md: "16px" },
              lineHeight: 1.4,
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
          fontFamily: "'Comic Neue', 'Comic Sans MS', cursive",
          fontSize: { xs: "16px", sm: "17px", md: "18px" },
          borderRadius: { xs: 2, sm: 3 },
          padding: { xs: "12px 24px", sm: "14px 28px", md: "16px 32px" },
          boxShadow:
            "0 8px 24px rgba(220, 38, 38, 0.3), 0 4px 12px rgba(0, 0, 0, 0.1)",
          border: "2px solid rgba(254, 202, 202, 0.6)",
          position: "relative",
          overflow: "hidden",
          transition: "all 0.3s ease-in-out",
          minHeight: { xs: "48px", sm: "52px", md: "56px" },
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
            transform: { xs: "none", sm: "translateY(-2px)" },
            "&::before": {
              left: "100%",
            },
          },
          "&:active": {
            transform: { xs: "none", sm: "translateY(0px)" },
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
