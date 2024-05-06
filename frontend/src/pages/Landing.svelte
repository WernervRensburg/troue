<script>
    import { Container } from "@sveltestrap/sveltestrap"
    import './static/landing.css'
</script>

<style>
    @font-face {
        font-family: 'RoxaleStory';
        font-style: normal;
        font-weight: 400;
        src: local('RoxaleStory') url(../fonts/RoxaleStory.ttf) format('truetype') url(../fonts/RoxaleStory.woff2) format('woff2');
    }

    .landing-name {
        font-family: 'RoxaleStory';
        font-size: 100px;
    }
</style>

<Container fluid class="landing-container">
    <h3 class="landing-name">
        Anja & Werner
    </h3>
</Container>
