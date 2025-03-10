import axios from "axios";

// API Base URL (Use environment variable for flexibility)
const API_BASE_URL = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000/api";

// Function to fetch all venues
export const getVenues = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/venues/`);
        return response.data; // If paginated, use response.data.results
    } catch (error) {
        console.error("Error fetching venues:", error);
        throw error;
    }
};

// Function to fetch a single venue by slug
export const getVenueDetails = async (slug) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/venues/${slug}/`);
        return response.data;
    } catch (error) {
        console.error(`Error fetching venue ${slug}:`, error);
        throw error;
    }
};

// Function to fetch events
export const getEvents = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/events/`);
        return response.data;
    } catch (error) {
        console.error("Error fetching events:", error);
        throw error;
    }
};
