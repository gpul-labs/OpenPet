<?php

namespace AppBundle\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Sensio\Bundle\FrameworkExtraBundle\Configuration\ParamConverter;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Request;

/**
 * @Route("/api/v1")
 */

class ApiV1Controller extends Controller
{

    // Specimens
    // -----------------------------------------

    /**
     * @Route("/specimens", name="api_v1_search_specimens")
     */
    public function searchSpecimenAction(Request $request)
    {
        // {{{

        $em = $this->getDoctrine()->getManager();

        $specimens = $em->getRepository('AppBundle:Specimen')->filter($request);

        $json = array();

        foreach ($specimens as $specimen) {
            $json[] = array(
                'id' => $specimen->getId(),
                'name' => $specimen->getName()
            );
        }

        return $this->json($json);

        // }}}
    }

    /**
     * @Route("/specimens/{id}", name="api_v1_get_specimen")
     * @ParamConverter("specimen", class="AppBundle:Specimen", options={"id" = "id"})
     */
    public function getSpecimenAction($specimen)
    {
        // {{{

        $json = array(
            'id' => $specimen->getId(),
            'name' => $specimen->getName(),
            'description' => $specimen->getDescription(),
            'summary' => $specimen->getSummary(),
            'image' => $specimen->getImage(),
            'sex' => $specimen->getSex(),
            'birthdate' => $specimen->getBirthdate()->format('Y-m-d'),
            'entrydate' => $specimen->getEntrydate()->format('Y-m-d'),
            'specie' => array(
                'id' => $specimen->getRace()->getSpecie()->getId(),
                'name' => $specimen->getRace()->getSpecie()->getName(),
            ),
            'race' => array(
                'id' => $specimen->getRace()->getId(),
                'name' => $specimen->getRace()->getName(),
            ),
            'origin' => array(
                'id' => $specimen->getOrigin()->getId(),
                'name' => $specimen->getOrigin()->getName(),
                'url' => $specimen->getOrigin()->getUrl(),
            ),
            'location' => array(
                'id' => $specimen->getLocation()->getId(),
                'name' => $specimen->getLocation()->getName(),
                'url' => $specimen->getLocation()->getUrl(),
                'latitude' => $specimen->getLocation()->getLatitude(),
                'longitude' => $specimen->getLocation()->getLongitude(),
            )
        );

        return $this->json($json);

        // }}}
    }

    // Provinces
    // -----------------------------------------

    /**
     * @Route("/provinces", name="api_v1_search_provinces")
     */
    public function searchProvinceAction(Request $request)
    {
        // {{{

        $em = $this->getDoctrine()->getManager();

        $provinces = $em->getRepository('AppBundle:Province')->filter($request);

        $json = array();

        foreach ($provinces as $province) {
            $json[] = array(
                'id' => $province->getId(),
                'name' => $province->getName()
            );
        }

        return $this->json($json);

        // }}}
    }

    // Species
    // -----------------------------------------

    /**
     * @Route("/species", name="api_v1_search_species")
     */
    public function searchSpecieAction(Request $request)
    {
        // {{{

        $em = $this->getDoctrine()->getManager();

        $species = $em->getRepository('AppBundle:Specie')->filter($request);

        $json = array();

        foreach ($species as $specie) {
            $json[] = array(
                'id' => $specie->getId(),
                'name' => $specie->getName()
            );
        }

        return $this->json($json);

        // }}}
    }

    // Races
    // -----------------------------------------

    /**
     * @Route("/races", name="api_v1_search_races")
     */
    public function searchRacesAction(Request $request)
    {
        // {{{

        $em = $this->getDoctrine()->getManager();

        $races = $em->getRepository('AppBundle:Race')->filter($request);

        $json = array();

        foreach ($races as $race) {
            $json[] = array(
                'id' => $race->getId(),
                'name' => $race->getName(),
                'specie' => array(
                    'id' => $race->getSpecie()->getId(),
                    'name' => $race->getSpecie()->getName(),
                )
            );
        }

        return $this->json($json);

        // }}}
    }

    // Locations
    // -----------------------------------------

    /**
     * @Route("/locations", name="api_v1_search_locations")
     */
    public function searchLocationAction(Request $request)
    {
        // {{{

        $em = $this->getDoctrine()->getManager();

        $locations = $em->getRepository('AppBundle:Location')->filter($request);

        $json = array();

        foreach ($locations as $location) {
            $json[] = array(
                'id' => $location->getId(),
                'name' => $location->getName()
            );
        }

        return $this->json($json);

        // }}}
    }

    /**
     * @Route("/locations/{id}", name="api_v1_get_location")
     * @ParamConverter("location", class="AppBundle:Location", options={"id" = "id"})
     */
    public function getLocationAction($location)
    {
        // {{{

        $json = array(
            'id' => $location->getId(),
            'name' => $location->getName(),
            'url' => $location->getUrl(),
            'phone' => $location->getPhone(),
            'latitude' => $location->getLatitude(),
            'longitude' => $location->getLongitude(),
            'province' => array(
                'id' => $location->getProvince()->getId(),
                'name' => $location->getProvince()->getName(),
            ),
        );

        return $this->json($json);

        // }}}
    }

    // Origins
    // -----------------------------------------

    /**
     * @Route("/origins", name="api_v1_search_origins")
     */
    public function searchOriginAction(Request $request)
    {
        // {{{

        $em = $this->getDoctrine()->getManager();

        $origins = $em->getRepository('AppBundle:Origin')->filter($request);

        $json = array();

        foreach ($origins as $origin) {
            $json[] = array(
                'id' => $origin->getId(),
                'name' => $origin->getName()
            );
        }

        return $this->json($json);

        // }}}
    }

    /**
     * @Route("/origins/{id}", name="api_v1_get_origin")
     * @ParamConverter("origin", class="AppBundle:Origin", options={"id" = "id"})
     */
    public function getOriginAction($origin)
    {
        // {{{

        $json = array(
            'id' => $origin->getId(),
            'name' => $origin->getName(),
            'url' => $origin->getUrl(),
        );

        return $this->json($json);

        // }}}
    }
}
