import React from 'react';
import HomeMaxIcon from '@mui/icons-material/HomeMax';
import ListIcon from '@mui/icons-material/List';
import NotListedLocationIcon from '@mui/icons-material/NotListedLocation';
import PermIdentityIcon from '@mui/icons-material/PermIdentity';
import InsertEmoticonIcon from '@mui/icons-material/InsertEmoticon';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';

export const sidebardata = [
    {
        title:"{user}",
        icon:<AccountCircleIcon />,
        link:""
    },
    {
        title:"Home",
        icon:<HomeMaxIcon />,
        link:"/home"
    },
    {
        title:"Show listings",
        icon:<ListIcon />,
        link:"/cum"
    },
    {
        title:"Create a listing",
        icon:<NotListedLocationIcon />,
        link:"/wow"
    },
    {
        title:"Current Requests",
        icon:<InsertEmoticonIcon />,
        link:"/uhoh"
    },
    {
        title:"Logout",
        icon:<PermIdentityIcon />,
        link:"/gaming"
    }
]