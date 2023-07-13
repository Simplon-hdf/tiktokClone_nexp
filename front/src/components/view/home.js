import React, {userEffect, userState} from "react";
import { UserProfile } from "../tools/profil";
import { BtnRond } from "../tools/btn";


export default function Home(parent){

    return (
        <>
        <div className="profil-content">
            <div className="profil-btn">
                <UserProfile /> 
                <BtnRond />
            </div>
        </div>
        </>
    );
}