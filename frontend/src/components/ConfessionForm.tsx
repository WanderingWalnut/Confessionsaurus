import React, { useState } from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import Select from "@mui/material/Select";
import type { SelectChangeEvent } from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import Checkbox from "@mui/material/Checkbox";
import FormControlLabel from "@mui/material/FormControlLabel";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";

interface ConfessionFormData {
  content: string;
  category?: string;
  isAnonymous: boolean;
}

const ConfessionForm: React.FC = () => {
  const [formData, setFormData] = useState<ConfessionFormData>({
    content: "",
    category: "",
    isAnonymous: true,
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError(null);

    try {
      // TODO: Implement API call
      console.log("Submitting confession:", formData);
      setFormData({
        content: "",
        category: "",
        isAnonymous: true,
      });
    } catch (err) {
      setError("Failed to submit confession. Please try again.");
      console.error("Error submitting confession:", err);
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    const target = e.target;
    const name = target.name;
    let value: string | boolean = target.value;
    if (target.type === "checkbox") {
      value = (target as HTMLInputElement).checked;
    }
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleCategoryChange = (event: SelectChangeEvent) => {
    setFormData((prev) => ({
      ...prev,
      category: event.target.value as string,
    }));
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
        value={formData.content}
        onChange={handleChange}
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
      <FormControl
        fullWidth
        sx={{
          "& .MuiOutlinedInput-root": {
            backgroundColor: "#222",
            color: "#fff",
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
      >
        <InputLabel id="category-label" sx={{ color: "#aaa" }}>
          Category
        </InputLabel>
        <Select
          labelId="category-label"
          id="category"
          name="category"
          value={formData.category}
          label="Category"
          onChange={handleCategoryChange}
          sx={{ color: "#fff" }}
          MenuProps={{
            PaperProps: {
              sx: {
                backgroundColor: "#222",
                color: "#fff",
              },
            },
          }}
        >
          <MenuItem value="">Select a category</MenuItem>
          <MenuItem value="academic">Academic</MenuItem>
          <MenuItem value="social">Social</MenuItem>
          <MenuItem value="personal">Personal</MenuItem>
          <MenuItem value="other">Other</MenuItem>
        </Select>
      </FormControl>
      <FormControlLabel
        control={
          <Checkbox
            id="isAnonymous"
            name="isAnonymous"
            checked={formData.isAnonymous}
            onChange={handleChange}
            color="primary"
            sx={{ color: "#aaa", "&.Mui-checked": { color: "#fff" } }}
          />
        }
        label="Post anonymously"
        sx={{ mb: 1, color: "#fff" }}
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
