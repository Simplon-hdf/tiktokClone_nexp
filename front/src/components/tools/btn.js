import React from "react";
import { BsPlusLg } from 'react-icons/bs';


export const BtnRond = () => {
    return (
        <>
        <button className="btn-rond btn">
            <BsPlusLg className="plus"/>
        </button>
        </>
    );
}

export function BtnCta() {
    return <button className="btn-cta btn">Connexion</button>;
}

export function BtnCta1() {
    return <button className="btn-cta btn">Inscription</button>;
}

export function InputDefault(iconpastille, labelreact){
    return (
        <>

        </>
    );
}

// export function btnCapsule({name}){
//     return (<button className="btn btn-capsule">`#${name}`</button>);
// }

