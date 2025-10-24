import { motion } from 'framer-motion';
import { format } from 'date-fns';

const EventCard = ({ event, onClose }) => {
  if (!event) return null;

  return (
    <motion.div
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: 50 }}
      className="fixed bottom-4 left-1/2 transform -translate-x-1/2 w-full max-w-md bg-white dark:bg-gray-800 rounded-lg shadow-xl p-6"
    >
      <button
        onClick={onClose}
        className="absolute top-4 right-4 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
      >
        <svg
          className="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>

      <div className="space-y-4">
        <div className="flex items-center space-x-2">
          <span className="px-2 py-1 text-xs font-semibold rounded-full"
            style={{ backgroundColor: event.epoch?.color || '#cbd5e1' }}
          >
            {event.epoch?.name || 'No Epoch'}
          </span>
          <span className="text-sm text-gray-500 dark:text-gray-400">
            {format(new Date(event.date), 'MMMM dd, yyyy')}
          </span>
        </div>

        <h3 className="text-xl font-bold text-gray-900 dark:text-white">
          {event.title}
        </h3>

        {event.location && (
          <div className="flex items-center text-gray-600 dark:text-gray-300">
            <svg
              className="w-4 h-4 mr-2"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
              />
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
              />
            </svg>
            <span>{event.location}</span>
          </div>
        )}

        <p className="text-gray-600 dark:text-gray-300">
          {event.description}
        </p>

        {event.categories?.length > 0 && (
          <div className="flex flex-wrap gap-2 mt-4">
            {event.categories.map(category => (
              <span
                key={category.id}
                className="px-2 py-1 text-xs font-semibold rounded-full"
                style={{ backgroundColor: category.color || '#e2e8f0' }}
              >
                {category.name}
              </span>
            ))}
          </div>
        )}

        {event.media_url && (
          <img
            src={event.media_url}
            alt={event.title}
            className="w-full h-48 object-cover rounded-lg mt-4"
          />
        )}

        <div className="flex items-center mt-4">
          <div className="flex-1">
            <div className="flex items-center">
              {[...Array(event.importance || 1)].map((_, i) => (
                <svg
                  key={i}
                  className="w-4 h-4 text-yellow-400"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                  />
                </svg>
              ))}
            </div>
            <span className="text-xs text-gray-500 dark:text-gray-400">
              Importance Level
            </span>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default EventCard;
