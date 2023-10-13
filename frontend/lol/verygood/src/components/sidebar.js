// import React from 'react';
// import "../App.css"
// import {sidebardata} from './sidebardata'

// function Sidebar(){
//     return(
//         <div className='Sidebar'>
//             <ul className='sidebarlist'>
//             {sidebardata.map((val,key)=>{
//                 return (
//                     <li 
//                     key={key} 
//                     className='row'
//                     id={window.location.pathname === val.link ? "active" : ""}
//                     onClick={() => {
//                         window.location.pathname=val.link;
//                         }}
//                     >
//                         <div id='icon'>{val.icon}</div><div id='title'>{val.title}</div>
//                     </li>
//                 );
//             })}
//             </ul>
//         </div>
//     )
// }

// export default Sidebar;


// Sidebar.js

import React from 'react';
import { Link } from 'react-router-dom'; // Import Link
import "../App.css";
import { sidebardata } from './sidebardata';

function Sidebar() {
  return (
    <div className='Sidebar'>
      <ul className='sidebarlist'>
        {sidebardata.map((val, key) => (
          <li key={key} className='row'>
            <Link to={val.link} className={window.location.pathname === val.link ? "active" : ""}>
              <div id='icon'>{val.icon}</div>
              <div id='title'>{val.title}</div>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Sidebar;

