import React, { useState } from 'react';
import axios from 'axios';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import TextareaAutosize from '@mui/material/TextareaAutosize';
import Button from '@mui/material/Button';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';

function CreateListings() {
  const [formData, setFormData] = useState({
    user_id: 16,
    quantity: '',
    food_type: 'prepared',
    description: '',
  });

  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState(null); // State for success message

  const handleChange = (e) => {
    const { name, value } = e.target;
    setError(null); // Clear any previous error
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Check if "Quantity" is a positive integer
    if (!/^[1-9][0-9]*$/.test(formData.quantity)) {
      setError('Quantity must be a positive integer.');
      return;
    }

    try {
      const response = await axios.post('http://localhost:8000/api/add_listing/', formData);
      setSuccessMessage(response.data.message); // Set success message on success
      setFormData({ ...formData, quantity: '', description: '' }); // Reset the form fields
    } catch (error) {
      setError(error.response.data.message);
    }
  };

  return (
    <Container maxWidth="sm">
      <Box mt={4}>
        <Typography variant="p" align="center" fontSize={20} gutterBottom>
          Create a New Listing:
        </Typography>
        <br /><br />
        <form onSubmit={handleSubmit}>
          <Box mb={2}>
            <TextField
              label="Source User ID"
              name="Source User ID"
              variant="outlined"
              fullWidth
              disabled
              value={formData.user_id}
            />
          </Box>
          <Box mb={2}>
            <TextField
              label="Quantity"
              name="quantity"
              variant="outlined"
              fullWidth
              value={formData.quantity}
              onChange={handleChange}
            />
          </Box>
          <Box mb={2}>
            <Select
              label="Food Type"
              name="food_type"
              variant="outlined"
              fullWidth
              value={formData.food_type}
              onChange={handleChange}
            >
              <MenuItem value="prepared">Prepared Food</MenuItem>
              <MenuItem value="groceries">Groceries</MenuItem>
            </Select>
          </Box>
          <Box mb={2}>
            <TextareaAutosize
              rowsMin={3}
              placeholder="Description"
              name="description"
              value={formData.description}
              onChange={handleChange}
              style={{ width: '100%' }}
            />
          </Box>
          {error && (
            <Box mb={2} color="error.main">
              {error}
            </Box>
          )}
          {successMessage && (
            <Box mb={2} color="success.main">
              {successMessage}
            </Box>
          )}
          <Box display="flex" justifyContent="center">
            <Button
              variant="outlined"
              color="primary"
              type="submit"
              style={{
                color: "black",
                borderColor: "black",
                borderRadius: 1,
              }}
            >
              Save Listing
            </Button>
          </Box>
        </form>
      </Box>
    </Container>
  );
}

export default CreateListings;
