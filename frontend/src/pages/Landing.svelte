<script>
  import landingBG from "../assets/images/landing.png";

  import Details from "./Details.svelte";

  let showDetailsPage = false;

  function showDetails() {
    showDetailsPage = !showDetailsPage;    
  }
</script>
{#if !showDetailsPage}
<div class="wrapper">
  <div class="left-section">
    <div class="image-container">
      <img
        class="landing-image"
        alt="The background for the main landing page"
        src={landingBG}
      />
    </div>
  </div>
  <div class="right-section">
    <div class="details-wrapper">
      <div class="invite">
        <span>Ons nooi jou uit na die huweliksvestiging van</span>
      </div>
      <div class="names">
        <span>Anja & Werner</span>
      </div>
      <div class="date">
        <span>Op 26 Oktober 2024</span>
      </div>
      <div class="location">
        <span>By Louvain Guest Farm, Herold</span>
      </div>
      <button on:click={showDetails} class="btn">Meer inligting</button>
    </div>
  </div>
</div>
{:else if showDetailsPage}
<Details />
{/if}

<style>
  @font-face {
    font-family: "QueenSides";
    src: url("/assets/fonts/QueenSides.ttf") format("truetype");
    font-display: swap;
  }
  @font-face {
    font-family: "EastLiberty";
    src: url("/assets/fonts/EastLiberty.ttf") format("truetype");
    font-display: swap;
  }

  .details-wrapper {
    margin: 5%;
    padding: 25px 0px 25px 0px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: azure;
    box-sizing: border-box;
  }

  .details-wrapper span {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    color: #ad925d;
    user-select: none;
  }

  .invite span {
    font-family: "QueenSides";
    font-size: 22px;
  }

  .names span {
    font-family: "EastLiberty";
    font-size: 60px;
  }

  .date span,
  .location span {
    font-family: "QueenSides";
    font-size: 18px;
  }

  .invite,
  .names,
  .date,
  .location {
    padding-bottom: 25px;
  }

  @media (min-width: 1000px) {
    .invite span {
      font-size: 26px;
    }

    .names span {
      font-size: 80px;
    }

    .date span,
    .location span {
      font-size: 24px;
    }
  }

  .wrapper {
    display: flex;
    flex-wrap: wrap;
  }

  .landing-image {
    display: block;
    width: 100%;
    height: auto;
    padding: 0;
    margin: 0;
  }

  .btn {
    border: 1px solid #ad925d;
    color: #ad925d;
    background-color: azure;
    cursor: pointer;
    font-family: "QueenSides";
    font-size: 22px;
    padding: 8px 20px 8px 20px;
    max-width: 8em;
  }

  .left-section {
    flex: 0 0 55%;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  .right-section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex: 0 0 45%;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    background-color: azure;
  }

  @media (max-width: 900px) {
    .wrapper {
      flex-direction: column !important;
    }

    .left-section,
    .right-section {
      flex: 0 0 100%;
    }
  }

  .btn:hover {
    background-color: azure;
    color: #ad925d;
  }
</style>
