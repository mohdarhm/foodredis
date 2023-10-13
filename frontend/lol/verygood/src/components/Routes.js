// Routes.js
import React from 'react';
import {Routes, Route, BrowserRouter } from 'react-router-dom';
import MainContent from './maincontent';
import ShowListings from './showlistings'; // Import other components
import Logout from './logout' 
import CreateListings from './createlistings';
import CurrentRequests from './currentrequests';

const Routess = () => {
  return (
    <Routes>
      <Route path="/home" element={<MainContent />} />
      <Route path="/showListings" element={<ShowListings />} />
      <Route path="/createlistings" element={<CreateListings />} />
      <Route path="/logout" element={<Logout />} />
      <Route path="/currentrequests" element={<CurrentRequests />} />
      {/* Define routes for other components as needed */}
      {/* <Redirect from="/" to="/home" /> */}
    </Routes>  );
};

export default Routess;
