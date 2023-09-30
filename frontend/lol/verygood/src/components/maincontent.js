import React from 'react';
import Sidebar from './sidebar';
import '../App.css'; // Import your CSS file
import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';
// import { Router } from 'react-router-dom'

const MainContent = () => {
  const user = 'Arhum';

  return (
    <div className="container">
      <Sidebar />
      <div className="content">
        {/* Content for the remaining space */}
        <div>
          <h1>Welcome, {user}!</h1>
        </div>
        <div>
          <br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br>
        </div>
        
        <div>
          <ul className='instructions'>
            <li><KeyboardArrowRightIcon />  This is the home page. relevant information may appear above.</li>
            <br></br>
            <li><KeyboardArrowRightIcon />  Get started by creating a listing now! once created, the listing can be seen by all distributors. A distributor may create a Request to you.</li>
            <br></br>
            <li><KeyboardArrowRightIcon />  Distributors can use "Show Listings" panel to find out whats available. They can then pick accordingly.</li>
            <br></br>
            <li><KeyboardArrowRightIcon />  As a source, you can also view current requests for you.</li>
            <br></br>
            <li><KeyboardArrowRightIcon />  Some buttons may be irrelevant to some type of users, in that case the panel will simply not run and display an error. Don't worry, its expected. the rest of the application</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default MainContent;
