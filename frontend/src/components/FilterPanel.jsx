import { useState } from 'react';
import { motion } from 'framer-motion';

const FilterPanel = ({
  categories,
  epochs,
  selectedCategories,
  selectedEpochs,
  onCategoryChange,
  onEpochChange,
  startDate,
  endDate,
  onDateChange
}) => {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <motion.div
      initial={{ x: -300 }}
      animate={{ x: isExpanded ? 0 : -270 }}
      className="fixed left-0 top-0 h-screen bg-white dark:bg-gray-800 shadow-lg z-10 w-72"
    >
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="absolute right-0 top-1/2 transform translate-x-12 -translate-y-1/2 bg-primary-500 text-white p-2 rounded-r-lg"
      >
        <svg
          className={`w-6 h-6 transform ${isExpanded ? 'rotate-180' : ''}`}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M9 5l7 7-7 7"
          />
        </svg>
      </button>

      <div className="p-6 h-full overflow-y-auto">
        <h2 className="text-xl font-bold mb-6 text-gray-900 dark:text-white">
          Filters
        </h2>

        {/* Date Range */}
        <div className="mb-6">
          <h3 className="text-sm font-semibold mb-2 text-gray-700 dark:text-gray-300">
            Date Range
          </h3>
          <div className="space-y-2">
            <input
              type="date"
              value={startDate}
              onChange={(e) => onDateChange(e.target.value, endDate)}
              className="w-full px-3 py-2 border rounded-md dark:bg-gray-700 dark:border-gray-600"
            />
            <input
              type="date"
              value={endDate}
              onChange={(e) => onDateChange(startDate, e.target.value)}
              className="w-full px-3 py-2 border rounded-md dark:bg-gray-700 dark:border-gray-600"
            />
          </div>
        </div>

        {/* Categories */}
        <div className="mb-6">
          <h3 className="text-sm font-semibold mb-2 text-gray-700 dark:text-gray-300">
            Categories
          </h3>
          <div className="space-y-2">
            {categories.map(category => (
              <label
                key={category.id}
                className="flex items-center space-x-2 cursor-pointer"
              >
                <input
                  type="checkbox"
                  checked={selectedCategories.includes(category.id)}
                  onChange={() => onCategoryChange(category.id)}
                  className="rounded text-primary-500 focus:ring-primary-500"
                />
                <span
                  className="text-sm text-gray-700 dark:text-gray-300"
                  style={{ color: category.color }}
                >
                  {category.name}
                </span>
              </label>
            ))}
          </div>
        </div>

        {/* Epochs */}
        <div className="mb-6">
          <h3 className="text-sm font-semibold mb-2 text-gray-700 dark:text-gray-300">
            Epochs
          </h3>
          <div className="space-y-2">
            {epochs.map(epoch => (
              <label
                key={epoch.id}
                className="flex items-center space-x-2 cursor-pointer"
              >
                <input
                  type="checkbox"
                  checked={selectedEpochs.includes(epoch.id)}
                  onChange={() => onEpochChange(epoch.id)}
                  className="rounded text-primary-500 focus:ring-primary-500"
                />
                <span
                  className="text-sm"
                  style={{ color: epoch.color }}
                >
                  {epoch.name}
                </span>
              </label>
            ))}
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default FilterPanel;
