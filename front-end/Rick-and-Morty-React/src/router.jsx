import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import CharactersPage from "./pages/CharactersPage";
import ErrorPage from "./pages/ErrorPage";
import CharacterPage from "./pages/CharacterDetailsPage";
import FavoritesPage from "./pages/FavoritesPage";

const router = createBrowserRouter([
    {
    path: "/",
    element: <App />,
    children: [
        {
            index: true,
            element: <HomePage />,
        },
        {
            path:'aboutus/',
            element: <AboutPage />,
        },
        {
            path:'characters/',
            element: <CharactersPage />
        },
        {
            path:'character/:id',
            element: <CharacterPage />
        },
        {
            path:'favorites/',
            element: <FavoritesPage />
        }
    ],
    errorElement: <ErrorPage/>
    },
],
);

export default router;