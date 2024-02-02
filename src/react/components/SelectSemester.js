

function SemesterItem({ title }) {
    const colorsCollections = ['bg-teal-400', 'bg-blue-400', 'bg-red-400', 'bg-green-400', 'bg-yellow-400', 'bg-indigo-400', 'bg-purple-400', 'bg-pink-400'];
    const bgColorCollections = ['bg-teal-500', 'bg-blue-500', 'bg-red-500', 'bg-green-500', 'bg-yellow-500', 'bg-indigo-500', 'bg-purple-500', 'bg-pink-500'];
    const positions = ['left-0', 'right-0'];
    const pickRandomPosition = positions[Math.floor(Math.random() * positions.length)];
    const pickColorItem = Math.floor(Math.random() * colorsCollections.length);
    const bgColor = colorsCollections[pickColorItem];
    const hoverBgColor = bgColorCollections[pickColorItem];

    return (
        <button
            className={`${bgColor} w-[10rem] mx-auto justify-center relative font-bold py-2 px-4 hover:shadow-md group rounded-md`}
        >
            <span className="z-20 text-white relative">{title}</span>
            <div className={`absolute h-full w-0 transition-all duration-500 rounded-md ease-in-out group-hover:w-full z-10 ${hoverBgColor} top-0 ${pickRandomPosition}`}></div>
        </button>
    );
};

export default function SelectSemester() {
    const semesterItems = [
        { id: 1, name: "Spring 2024", value: "Spring-2024" },
        { id: 2, name: "Fall 2024", value: "Fall-2024" },
        { id: 3, name: "Summer 2024", value: "Summer-2024" },
        { id: 4, name: "Spring 2025", value: "Spring-2025" },
    ];
    return <div className="mt-12">
        <div className="w-[40rem] overflow-x-auto">
            <div className="flex flex-col md:flex-row space-y-3 md:space-y-0 md:space-x-4">
                {
                    semesterItems.length > 0 && semesterItems.map((item) => {
                        return <SemesterItem title={item.name} key={item.id} />
                    })
                }
            </div>
        </div>
    </div>;
}
