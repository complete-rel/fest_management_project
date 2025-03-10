import React, { useEffect, useState } from "react";
import { getVenues } from "../api/api"; // Import API service

const VenueList = () => {
    const [venues, setVenues] = useState([]);

    useEffect(() => {
        const fetchVenues = async () => {
            try {
                const data = await getVenues();
                setVenues(data.results);  // If paginated
            } catch (error) {
                console.error("Failed to fetch venues", error);
            }
        };

        fetchVenues();
    }, []);

    return (
        <div>
            <h2>Venues</h2>
            <ul>
                {venues.map(venue => (
                    <li key={venue.slug}>
                        <h3>{venue.name}</h3>
                        <p>{venue.address}</p>
                        <a href={venue.google_maps_url} target="_blank" rel="noopener noreferrer">Get Directions</a>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default VenueList;
