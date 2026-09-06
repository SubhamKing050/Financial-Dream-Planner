import { useState } from "react";

function InputForm({ onSubmit, loading }) {
    const [formData, setFormData] = useState({
        age: 25,
        city: "Bangalore",
        area_type: "Central",
        education: "B.Tech",
        job_role: "Software Engineer",
        current_salary: 50000,
        saving_percentage: 20,
        marriage_years: 5,
        car_years: 4,
        home_years: 10
    });

    function handleChange(event) {
        const { name, value } = event.target;

        setFormData({
            ...formData,
            [name]: value
        });
    }

    function handleSubmit(event) {
        event.preventDefault();

        const data = {
            ...formData,
            age: Number(formData.age),
            current_salary: Number(formData.current_salary),
            saving_percentage: Number(formData.saving_percentage),
            marriage_years: Number(formData.marriage_years),
            car_years: Number(formData.car_years),
            home_years: Number(formData.home_years)
        };

        onSubmit(data);
    }

    return (
        <section className="input-section">
            <div className="section-heading">
                <span>01</span>
                <div>
                    <h2>Your Financial Profile</h2>
                    <p>
                        Tell us about yourself and your financial goals.
                    </p>
                </div>
            </div>

            <form onSubmit={handleSubmit} className="financial-form">

                <div className="form-grid">

                    <div className="form-group">
                        <label>Age</label>
                        <input
                            type="number"
                            name="age"
                            value={formData.age}
                            onChange={handleChange}
                            min="18"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>City</label>
                        <input
                            type="text"
                            name="city"
                            value={formData.city}
                            onChange={handleChange}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Area Type</label>
                        <select
                            name="area_type"
                            value={formData.area_type}
                            onChange={handleChange}
                        >
                            <option value="Central">Central</option>
                            <option value="Suburban">Suburban</option>
                            <option value="Rural">Rural</option>
                        </select>
                    </div>

                    <div className="form-group">
						<label>Education</label>

						<select
							name="education"
							value={formData.education}
							onChange={handleChange}
							required
						>
							<option value="High School">High School</option>
							<option value="Diploma">Diploma</option>
							<option value="B.Sc">B.Sc</option>
							<option value="M.Sc">M.Sc</option>
							<option value="B.Tech">B.Tech</option>
							<option value="M.Tech">M.Tech</option>
							<option value="BBA">BBA</option>
							<option value="MBA">MBA</option>
							<option value="Other">Other</option>
						</select>
					</div>

                    <div className="form-group">
                        <label>Job Role</label>
                        <input
                            type="text"
                            name="job_role"
                            value={formData.job_role}
                            onChange={handleChange}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Current Monthly Salary</label>
                        <input
                            type="number"
                            name="current_salary"
                            value={formData.current_salary}
                            onChange={handleChange}
                            min="0"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Saving Percentage</label>
                        <input
                            type="number"
                            name="saving_percentage"
                            value={formData.saving_percentage}
                            onChange={handleChange}
                            min="1"
                            max="100"
                            required
                        />
                    </div>

                </div>

                <div className="goals-heading">
                    <h3>Your Dream Timelines</h3>
                    <p>When would you like to achieve these goals?</p>
                </div>

                <div className="goals-grid">

                    <div className="goal-input">
                        <img
							src="/images/marriage.png"
							alt="Marriage"
							className="goal-image"
						/>
                        <div>
                            <label>Marriage</label>
                            <div className="year-input">
                                <input
                                    type="number"
                                    name="marriage_years"
                                    value={formData.marriage_years}
                                    onChange={handleChange}
                                    min="1"
                                    required
                                />
                                <span>years</span>
                            </div>
                        </div>
                    </div>

                    <div className="goal-input">
                        <img
							src="/images/car.png"
							alt="Car"
							className="goal-image"
						/>
                        <div>
                            <label>Car</label>
                            <div className="year-input">
                                <input
                                    type="number"
                                    name="car_years"
                                    value={formData.car_years}
                                    onChange={handleChange}
                                    min="1"
                                    required
                                />
                                <span>years</span>
                            </div>
                        </div>
                    </div>

                    <div className="goal-input">
                        <img
							src="/images/home.png"
							alt="Home"
							className="goal-image"
						/>
                        <div>
                            <label>Home</label>
                            <div className="year-input">
                                <input
                                    type="number"
                                    name="home_years"
                                    value={formData.home_years}
                                    onChange={handleChange}
                                    min="1"
                                    required
                                />
                                <span>years</span>
                            </div>
                        </div>
                    </div>

                </div>

                <button
                    type="submit"
                    className="generate-button"
                    disabled={loading}
                >
                    {loading
                        ? "Generating Plan..."
                        : "Generate My Financial Plan"}
                </button>

            </form>
        </section>
    );
}

export default InputForm;