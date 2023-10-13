import "./App.css";
import React, { useState, useEffect } from "react";
import Maincontent from "./components/maincontent";

function App() {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null); // State to store the error message

  useEffect(() => {
    const checkAuthentication = async () => {
      try {
        const response = await fetch("http://localhost:8000/check-auth");
        if (response.ok) {
          const userData = await response.json();
          setUser(userData.user);
        } else {
          // Handle the case when the server returns an error status
          setError("Authentication error. Please try again.");
        }
      } catch (error) {
        // Handle network or other errors
        setError("An error occurred. Please try again later.");
        console.error("An error occurred:", error);
      }
    };

    // checkAuthentication();
  }, []);

  return (
    <div className="App">
  <Maincontent />
    </div>
  );
}

export default App;



// import "./App.css";
// import React, { useState, useEffect } from "react";
// import Maincontent from "./components/maincontent";

// function App() {
//   const [user, setUser] = useState(null);
//   const [apiResponse, setApiResponse] = useState(null); // State to store the API response
//   const [error, setError] = useState(null); // State to store any errors

//   useEffect(() => {
//     const checkAuthentication = async () => {
//       try {
//         const response = await fetch("http://localhost:8000/check-auth",{
//         method:"POST",
//         body:""
//         });
//         const jsonData = await response.json();

//         if (response.ok) {
//           setUser(jsonData.user);
//         } else {
//           // Handle the case when the server returns an error status
//           setError(`HTTP Status Code: ${response.status}\n${jsonData.message}`);
//         }

//         // Store the entire JSON response for display
//         setApiResponse(jsonData);
//       } catch (error) {
//         // Handle network or other errors
//         setError("An error occurred. Please try again later.");
//         console.error("An error occurred:", error);
//       }
//     };

//     checkAuthentication();
//   }, []);

//   return (
//     <div className="App">
//       {error ? (
//         <div>
//           <p>{error}</p>
//         </div>
//       ) : user ? (
//           <Maincontent />
//       ) : (
//         <div>
//           <p>That didnt work. kindly login</p>
//           {/* Render content for non-authenticated users */}
//         </div>
//       )};
//     </div>
//   );
// }
// export default App;
