<script>

  import landingBG from "/assets/images/landing3.JPG";

  function showDetails() {}
</script>

<div class="wrapper">
  <div class="left-section">
    <div class="details-container">
      <img alt="The background for the main landing page" src={landingBG} />
    </div>
  </div>
  <div class="right-section">
    <div class="header-wrapper">
    </div>
    <div class="options-wrapper">
    <button on:click={showDetails} class="btn">Meer inligting</button>
    </div>
  </div>
</div>

<style>
  @font-face {
    font-family: "RoxaleStory";
    src: url("/assets/fonts/RoxaleStory.ttf") format("truetype"); /* Corrected format */
    font-display: swap;
  }
  @font-face {
    font-family: "EastLiberty";
    src: url("/assets/fonts/EastLiberty.ttf") format("truetype"); /* Corrected format */
    font-display: swap;
  }

  .wrapper {
    border: 1px solid red;
    display: flex;
    flex-wrap: wrap;
  }

  .btn {
    border: 1px solid #ad925d;
    color: #ad925d;
    cursor: pointer;
    font-family: "RoxaleStory";
    font-size: 22px;
    padding: 8px 20px 8px 20px;
  }

  .left-section {
    flex: 0 0 55%;
    border: 1px solid green;
    box-sizing: border-box;
  }

  .right-section {
    flex: 0 0 45%;
    border: 1px solid black;
    box-sizing: border-box;
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
    background-color: initial;
    color: #ad925d;
  }

  :global(body) {
    background-size: contain;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
  }
</style>
