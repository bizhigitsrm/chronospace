import { useState, useEffect } from 'react';
import axios from 'axios';
import { AnimatePresence } from 'framer-motion';
import TimeLine3D from './components/TimeLine3D';
import EventCard from './components/EventCard';
import FilterPanel from './components/FilterPanel';

const API_BASE_URL = import.meta.env.VITE_API_URL;

function App() {
  const [events, setEvents] = useState([]);
  const [categories, setCategories] = useState([]);
  const [epochs, setEpochs] = useState([]);
  const [selectedEvent, setSelectedEvent] = useState(null);
  const [selectedCategories, setSelectedCategories] = useState([]);
  const [selectedEpochs, setSelectedEpochs] = useState([]);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch initial data
  useEffect(() => {
    const fetchData = async () => {
      try {
        const [eventsRes, categoriesRes, epochsRes] = await Promise.all([
          axios.get(`${API_BASE_URL}/events`),
          axios.get(`${API_BASE_URL}/categories`),
          axios.get(`${API_BASE_URL}/epochs`)
        ]);

        setEvents(eventsRes.data);
        setCategories(categoriesRes.data);
        setEpochs(epochsRes.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch data');
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Filter events when filters change
  useEffect(() => {
    const fetchFilteredEvents = async () => {
      try {
        let params = new URLSearchParams();

        if (selectedCategories.length > 0) {
          selectedCategories.forEach(id => params.append('category_id', id));
        }
        if (selectedEpochs.length > 0) {
          selectedEpochs.forEach(id => params.append('epoch_id', id));
        }
        if (startDate) params.append('start_date', startDate);
        if (endDate) params.append('end_date', endDate);

        const response = await axios.get(`${API_BASE_URL}/events?${params}`);
        setEvents(response.data);
      } catch (err) {
        setError('Failed to fetch filtered events');
      }
    };

    fetchFilteredEvents();
  }, [selectedCategories, selectedEpochs, startDate, endDate]);

  const handleCategoryChange = (categoryId) => {
    setSelectedCategories(prev =>
      prev.includes(categoryId)
        ? prev.filter(id => id !== categoryId)
        : [...prev, categoryId]
    );
  };

  const handleEpochChange = (epochId) => {
    setSelectedEpochs(prev =>
      prev.includes(epochId)
        ? prev.filter(id => id !== epochId)
        : [...prev, epochId]
    );
  };

  const handleDateChange = (start, end) => {
    setStartDate(start);
    setEndDate(end);
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-primary-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="text-red-500 text-center">
          <h2 className="text-2xl font-bold mb-2">Error</h2>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="relative h-screen overflow-hidden bg-gray-900">
      <FilterPanel
        categories={categories}
        epochs={epochs}
        selectedCategories={selectedCategories}
        selectedEpochs={selectedEpochs}
        onCategoryChange={handleCategoryChange}
        onEpochChange={handleEpochChange}
        startDate={startDate}
        endDate={endDate}
        onDateChange={handleDateChange}
      />

      <TimeLine3D
        events={events}
        onEventClick={setSelectedEvent}
      />

      <AnimatePresence>
        {selectedEvent && (
          <EventCard
            event={selectedEvent}
            onClose={() => setSelectedEvent(null)}
          />
        )}
      </AnimatePresence>
    </div>
  );
}

export default App;
