<script>

  let rsvpStage = 0;

  let postData = {
    'name': 'Jaco van Rensburg',
  };
  let responseData = null;

  async function findInvite() {
    rsvpStage += 1;

    try {
      const response = await fetch('http://127.0.0.1:5000/guests/find_guest?format=json', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
      });

      responseData = await response.json();
      console.log(responseData);

    } catch (error) {
      console.log(error);
    }
  }

  async function updateGuestAttendance() {
    rsvpStage += 1;

    try {
      const response = await fetch('http://127.0.0.1:5000/guests/update_guest_attendance?format=json', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
      });

      const data = await response.json();
      console.log(data);

    } catch (error) {
      console.log(error);
    }
  }

  async function updateGuestAccommodation() {
    rsvpStage += 1;

    try {
      const response = await fetch('http://127.0.0.1:5000/guests/update_guest_accommodation?format=json', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
      });

      const data = await response.json();
      console.log(data);

    } catch (error) {
      console.log(error);
    }
  }

  async function updateGuestEmail() {
    rsvpStage += 1;

    try {
      const response = await fetch('http://127.0.0.1:5000/guests/update_guest_accommodation?format=json', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
      });

      const data = await response.json();
      console.log(data);

    } catch (error) {
      console.log(error);
    }
  }

  function increaseRsvpStage() {
    rsvpStage += 1;
  }

  function resetRSVP() {
    rsvpStage = 0;
  }

</script>

<div class="rsvp-wrapper">
  {#if rsvpStage === 0}
    
  <div class="find-inv-wrapper">
    <p class="rsvp-desc">
      Indien jy vir jou en <span class="comma">'</span>n gas RSVP<span class="comma">(</span>of jou familie<span class="comma">),</span> sal jy kan RSVP vir die hele groep.
    </p>
    <div class="form">
      <input class="fn-input" placeholder="Volle Naam en Van" />
      <button class="find-invite-btn" on:click={findInvite}>Vind Jou Uitnodiging</button>
    </div>
  </div>
  {:else if rsvpStage === 1}
  <div class="found-inv-wrapper">
    {responseData}
    
    <button class="find-invite-btn" on:click={increaseRsvpStage}>Volgende</button>
    <button class="find-invite-btn" on:click={resetRSVP}>Soek Weer</button>
  </div>
  {:else if rsvpStage === 2}
  <div class="attendance-wrapper">
    Wie kom almal saam?
    <!-- Doen accepted / declined vir al die gaste + vir +1's sit 'n button by om +1 te select, if selected - form field vir naam -->
    <button class="find-invite-btn" on:click={updateGuestAttendance}>Volgende</button>
    <button class="find-invite-btn" on:click={resetRSVP}>Begin Voor</button>
  </div>
  {:else if rsvpStage === 3}
  <div class="accommodation-wrapper">
    Kies jou verblyf opsies
    <button class="find-invite-btn" on:click={updateGuestAccommodation}>Volgende</button>
    <button class="find-invite-btn" on:click={resetRSVP}>Begin Voor</button>
  </div>
  {:else if rsvpStage === 4}
  <div class="email-wrapper">
    Epos addres - baie belangrik sodat Louvain die faktuur vir die verblyf na jou kan stuur
    <button class="find-invite-btn" on:click={updateGuestEmail}>Volgende</button>
    <button class="find-invite-btn" on:click={resetRSVP}>Begin Voor</button>
  </div>
  {:else if rsvpStage === 5}
  <div class="rsvp-done">
    Ons sien uit om ons spesiale dag met julle te deel!

    Daar sal 'n epos gestuur word om die RSVP te bevestig.
  </div>
  <div>

  </div>
  {/if}
</div>

<style>
  .rsvp-wrapper {
    border: 1px solid green;
  }

  .found-inv-wrapper,
  .attendance-wrapper,
  .email-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .rsvp-desc {
    border: 1px solid red;
  }

  .form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .fn-input,
  .find-invite-btn {
    margin: 15px 0px 15px 0px;
    width: 450px;
    box-sizing: border-box;
  }
</style>