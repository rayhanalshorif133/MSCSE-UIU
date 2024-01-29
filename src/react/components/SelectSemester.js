const SemesterItem = () => {
    return (
        <div className="flex flex-col">
            hll
        </div>
    );
};

export default function SelectSemester() {
    const title = "Select Semester";
    const bgColor = "bg-green-500";
    return <div className="mt-32">
        <div className="flex space-x-4">
            {/* <SemesterItem title="Fall 2021" /> */}
            <button
                className={`${bgColor} hover:bg-green-700 text-white font-bold py-2 px-4 rounded`}
            >
                {title}
            </button>
        </div>
    </div>;
}
