<?php

namespace AppBundle\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Sensio\Bundle\FrameworkExtraBundle\Configuration\Template;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Request;

class DefaultController extends Controller
{

    /**
     * @Route("/", name="homepage")
     * @Template("default/index.html.twig")
     */
    public function indexAction(Request $request)
    {
        // {{{

        $em = $this->getDoctrine()->getManager();

        return array(
            'specimenTotal' => $em->getRepository('AppBundle:Specimen')->getTotalCount(),
            'specimens' => $em->getRepository('AppBundle:Specimen')->filter($request, 25),
            'locations' => $em->getRepository('AppBundle:Location')->filter($request, 100),
            'races' => $em->getRepository('AppBundle:Race')->filter($request, 100),
        );

        // }}}
    }

    /**
     * @Route("/api", name="api_description")
     * @Template("default/api.html.twig")
     */
    public function apiAction(Request $request)
    {
        // {{{
        // }}}
    }

}
