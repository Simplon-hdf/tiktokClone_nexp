import {Route, Routes} from "react-router-dom"
import Home from "./view/home"
import Login from "./view/login"
import Subscription from "./view/subscription"
import NewVideo from "./view/newVideo"

export default function Main(data){
    return (
        <div>
            <Routes>
                <Route path="/" element={<Login/>}/>
                <Route path="/signup" element={<Subscription/>}/>
                <Route path="/:idvideo" element={<Home/>}/>
                <Route path="/:token/new" element={<NewVideo/>}/>
            </Routes>
        </div>
    )
}