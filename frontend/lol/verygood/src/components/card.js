import React from "react";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import StarRateIcon from "@mui/icons-material/StarRate";

const Card = ({ data }) => {
  return (
    <div classname='cards'>
        <br />
      <img src="https://picsum.photos/300/200" alt="cardimg" />
      <Typography variant="h5">{data.listings__description}</Typography>
      <Typography variant="subtitle1">
        <strong>Quantity:</strong> {data.listings__quantity}
      </Typography>
      <Typography variant="subtitle2">
        <strong>Email:</strong> {data.email}
      </Typography>
      <Typography variant="subtitle2">
        <strong>Phone No:</strong> {data.phoneno}
      </Typography>
      <Typography variant="subtitle2">
        <strong>Source Name:</strong> {data.name}
      </Typography>
      <Typography variant="subtitle2">{data.address}</Typography>
      <Typography variant="caption">
        <StarRateIcon fontSize="small" /> {getStarRating(data.ratings)}
      </Typography>
      <br></br><br></br>
      <Button
        style={{
          color: "black",
          borderColor: "black",
          borderRadius: 15,
        }}
        variant="outlined"
      >
        CONTACT THEM!
      </Button>
    </div>
  );
};

// Function to calculate star ratings based on the rating value
const getStarRating = (ratings) => {
  const ratingValue = parseFloat(ratings);
  if (ratingValue <= 1) {
    return "1 Star";
  } else {
    return `${Math.round(ratingValue)} Stars`;
  }
};

export default Card;
