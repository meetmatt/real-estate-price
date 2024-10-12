import { FormEvent, useState } from "react";

interface Data {
  area: number;
  bedrooms: number;
  predicted_price: number;
}

export default function App() {
  const [price, setPrice] = useState<number | null>(null);
  const [area, setArea] = useState(65);
  const [bedrooms, setBedrooms] = useState(1);

  function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ area, bedrooms }),
    };

    fetch("/api/predict", requestOptions)
      .then((response) => response.json())
      .then((data: Data) => setPrice(data.predicted_price))
      .catch((error) => alert(error));
  }

  return (
    <>
      <h2>Price calculator</h2>
      <div>
        <form onSubmit={handleSubmit}>
          <div className="input">
            <label htmlFor="area">Area in square meters</label>
            <input
              type="number"
              name="area"
              id="area"
              placeholder="Area in square meters"
              value={area}
              onChange={(e) => setArea(Number(e.target.value))}
            />
          </div>
          <div className="input">
            <label htmlFor="area">Number of bedrooms</label>
            <input
              type="number"
              name="bedrooms"
              placeholder="Number of bedrooms"
              value={bedrooms}
              onChange={(e) => setBedrooms(Number(e.target.value))}
            />
          </div>
          <button>Submit</button>
        </form>
      </div>
      {price !== null && <div>Price: €{price}</div>}
    </>
  );
}
