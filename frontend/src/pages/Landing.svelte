<script>
  function showDetails() {}
</script>

<div class="landing">
  <!-- <div class="sm-cont">
    <h4 class="sm-txt">Ons nooi jou uit na die huweliksvestiging van</h4>
  </div>
  <div class="sm-cont">
    <h3 class="names">Anja & Werner</h3>
  </div>
  <div class="sm-cont">
    <h4 class="md-txt">Op 26 Oktober 2024</h4>
  </div>
  <div class="sm-cont">
    <h4 class="sm-txt">By Louvain Guest Farm</h4>
  </div> -->
  <button on:click={showDetails} class="btn">Meer inligting</button>
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

  .landing {
    place-content: center;
    place-items: center;
  }

  .sm-cont {
    width: fit-content;
    margin: auto;
  }

  .names {
    font-family: "EastLiberty";
    font-size: 100px;
    color: #ad925d;
  }

  .md-txt {
    font-family: "RoxaleStory";
    font-size: 30px;
    color: #ad925d;
    width: auto;
  }

  .sm-txt {
    font-family: "RoxaleStory";
    font-size: 20px;
    color: #ad925d;
  }

  .btn {
    border: 1px solid #ad925d;
    color: #ad925d;
    cursor: pointer;
    font-family: "RoxaleStory";
    font-size: 22px;
    padding: 8px 20px 8px 20px;
  }

  .btn:hover {
    background-color: initial;
    color: initial;
  }

  :global(body) {
    background-size: contain;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
  }
</style>
