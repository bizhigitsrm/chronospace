import { useRef, useState, useEffect } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Text } from '@react-three/drei';
import { format } from 'date-fns';
import { motion } from 'framer-motion';

const EventPoint = ({ event, position, onClick }) => {
  const [hovered, setHovered] = useState(false);

  return (
    <group
      position={position}
      onClick={() => onClick(event)}
      onPointerOver={() => setHovered(true)}
      onPointerOut={() => setHovered(false)}
    >
      <mesh>
        <sphereGeometry args={[0.2, 32, 32]} />
        <meshStandardMaterial
          color={hovered ? "#38bdf8" : "#0ea5e9"}
          emissive={hovered ? "#38bdf8" : "#0ea5e9"}
          emissiveIntensity={hovered ? 0.5 : 0.2}
        />
      </mesh>
      <Text
        position={[0, 0.5, 0]}
        fontSize={0.3}
        color="#ffffff"
        anchorX="center"
        anchorY="bottom"
      >
        {event.title}
      </Text>
      {hovered && (
        <Text
          position={[0, -0.5, 0]}
          fontSize={0.2}
          color="#ffffff"
          anchorX="center"
          anchorY="top"
        >
          {format(new Date(event.date), 'MMM dd, yyyy')}
        </Text>
      )}
    </group>
  );
};

const TimeLine3D = ({ events, onEventClick }) => {
  const controlsRef = useRef();

  const timelineLength = 20;
  const maxEvents = events.length;

  // Sort events by date
  const sortedEvents = [...events].sort((a, b) =>
    new Date(a.date).getTime() - new Date(b.date).getTime()
  );

  // Calculate positions based on dates
  const positions = sortedEvents.map((event, index) => {
    const x = (index / (maxEvents - 1)) * timelineLength - timelineLength / 2;
    const y = Math.sin(index * 0.5) * 2; // Add some vertical variation
    const z = Math.cos(index * 0.5) * 2; // Add some depth variation
    return [x, y, z];
  });

  return (
    <div className="w-full h-screen">
      <Canvas camera={{ position: [0, 5, 15], fov: 60 }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} intensity={1} />

        {/* Timeline base */}
        <mesh position={[0, -2, 0]} rotation={[0, 0, 0]}>
          <boxGeometry args={[timelineLength, 0.1, 0.1]} />
          <meshStandardMaterial color="#1e293b" />
        </mesh>

        {/* Event points */}
        {sortedEvents.map((event, index) => (
          <EventPoint
            key={event.id}
            event={event}
            position={positions[index]}
            onClick={onEventClick}
          />
        ))}

        <OrbitControls
          ref={controlsRef}
          enablePan={true}
          enableZoom={true}
          enableRotate={true}
          minDistance={5}
          maxDistance={30}
        />
      </Canvas>
    </div>
  );
};

export default TimeLine3D;
