import React from "react";
import { BiComment } from 'react-icons/bi';
import { HiOutlineHeart } from 'react-icons/hi';
const profilePicture = require.context("../pictures", true);



export function UserProfile({pseudo, description}){
  
  let likeCount = 1205;
  // let profilePicture = "../pictures/profilePicture1.jpg";
  let commentCount = 653;

    return (
      <>
        <div className="profile-image">
          <img src={profilePicture("./profilePicture1.jpg")} alt="Profil"></img>
        </div>

       <div className="user-info">

        <div className="pseudonyme">{pseudo}</div>

        <div className="action">
            <span className="comment-count">
                <BiComment />
                {commentCount}
            </span>
            <span className="likes-count">
                <HiOutlineHeart />
                {likeCount}
            </span>
            
        </div>
       </div>

       <div className="description">
            {description}
       </div>
      </>
    );
  };