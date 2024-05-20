<script>
  import FlipClock from "svelte-flip-clock";

  import { onMount } from "svelte";

  const targetDate = new Date("2024-10-26T16:00:00");

  let myCustomDate = new Date();
  
  function updateCountdown() {
    const now = new Date();
    const timeRemaining = targetDate.getTime() - now.getTime(); // Use getTime() to get the time in milliseconds

    if (timeRemaining > 0) {
      const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

      myCustomDate.setHours(hours);
      myCustomDate.setMinutes(minutes);
      myCustomDate.setSeconds(seconds);
    } else {
      // Countdown complete
      myCustomDate.setHours(0);
      myCustomDate.setMinutes(0);
      myCustomDate.setSeconds(0);
    }
  }

  let interval;
  onMount(() => {
    interval = setInterval(updateCountdown, 1000);
    return () => {
      clearInterval(interval);
    };
  });

</script>

<div class="main-wrapper">
  <div class="main-details-wrapper">
    <span class="main-header">Die Details</span>
    <div class="vd-wrapper">
      <div class="vd-left"></div>
      <div class="vd-right"></div>
    </div>
    <div class="when-icon">
      <i class="fa-regular fa-clock d-icon fa-2xl"></i>
    </div>
    <div class="when">26 Oktober 2024, 04<span class="comma">:</span>00 PM</div>
    <div class="countdown">
      <FlipClock
        bind:date={myCustomDate}
        showHours={true}
        showMinutes={true}
        showSeconds={true}
        size={1}
        textColor="white"
        backgroundColor="#383838"
      />
    </div>
    <div class="where-icon">ICON</div>
    <div class="where">
      Louvain Guest Farm<span class="comma">,</span> Herold
    </div>
    <div class="directions">EMBED MAPS</div>
    <div class="venue-photos">VENUE IMAGES</div>
  </div>
  <div class="other-details-wrapper">
    <div class="accomodation"></div>
    <div class="more-details"></div>
    <div class="friday-event"></div>
    <div class="dresscode"></div>
    <div class="rsvp"></div>
    <div class="registry"></div>
  </div>
</div>

<style>
  .main-wrapper {
    display: flex;
    border: 1px solid green !important;
    flex-direction: column;
    align-items: center;
  }

  .main-wrapper div {
    border: 1px solid red;
    box-sizing: border-box;
    max-width: 1000px;
    width: 100%;
    padding: 10px;
  }

  .main-details-wrapper {
    background-color: azure;
    display: flex;
    flex-direction: column;
  }

  .vd-wrapper {
    display: flex;
  }

  .vd-right,
  .vd-left {
    height: 55px;
  }

  .vd-right {
    border-left: 1px solid #ad925d !important;
  }

  .vd-left {
    border-right: 1px solid #ad925d !important;
  }

  .d-icon {
    color: #ad925d !important;
  }

  .main-header {
    font-size: 28px;
  }

  .where {
    font-size: 18px;
  }

  .main-header,
  .where,
  .when {
    font-family: "RoxaleStory";
    color: #ad925d;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  }

  .comma {
    font-family: "Times New Roman", Times, serif !important;
  }
</style>
